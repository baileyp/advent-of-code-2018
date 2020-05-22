from collections import defaultdict, deque
from functools import partial


def part1(file):
    """
    O(n) space and O(e log e + n) time where n is the number of instructions (nodes) and e is the number of edges in the
    graph
    :param file:
    :return:
    """
    graph, heads = build_graph(file)
    path = walk_node(heads, graph, deque())
    return ''.join(path)


def part2(file, instruction_base_time=60, num_workers=4):
    """
    O(n) space and O(e log e + n) time where n is the number of instructions (nodes) and e is the number of edges in the
    graph
    :param file:
    :param instruction_base_time:
    :param num_workers:
    :return:
    """
    factory = partial(TimedInstruction.from_instruction, base_time=instruction_base_time)
    graph, heads = build_graph(file)
    graph = {k: list(map(factory, v)) for (k, v) in graph.items()}
    heads = list(map(factory, heads))

    return walk_node_pooled(heads, graph, WorkerPool(num_workers))


def build_graph(file):
    # Build an adjacency list graph
    graph = defaultdict(lambda: list())
    instructions = iter((line[5], line[36]) for line in file)
    # Also track all child nodes
    child_nodes = set()
    for first, second in instructions:
        child_nodes.add(second)
        graph[first].append(second)

    # Sort the graph by parent node
    graph = {k: v for (k, v) in sorted(graph.items())}

    # Find all the head nodes, i.e., those without any parents
    heads = (set(graph.keys()) ^ child_nodes) & set(graph.keys())

    return graph, heads


def walk_node(available, graph, path):
    # All parent instructions have been executed, only the last instruction remains
    if len(graph) == 0:
        path.append(available.pop())
        return path

    # For each available instruction
    # - Add it to the path
    # - Make it no longer available and remove it from the graph
    # - Merge its children with the other available instructions
    for node in sorted(available):
        if not is_available(node, graph):
            continue
        path.append(node)
        available.remove(node)
        available = set(list(available) + graph[node])
        graph.pop(node)
        break

    # Again!
    return walk_node(available, graph, path)


def walk_node_pooled(available, graph, worker_pool, elapsed=0):
    # All parent instructions have been executed, only the last instruction remains
    if len(graph) == 0:
        return elapsed + available.pop().duration

    # Assign as many instructions as possible to the available workers
    for instruction in sorted(available):
        if is_available(instruction, graph) and worker_pool.is_assignable(instruction):
            worker_pool.assign(instruction)

    # For each completed instruction coming from the worker pool
    # - Make it no longer available and remove it from the graph
    # - Merge its children with the other available instructions
    for completed in worker_pool.tick():
        available.remove(completed)
        available = set(list(available) + graph[completed.instruction])
        graph.pop(completed.instruction)

    # Do it again, adding the elapsed time from the worker pool to the overall elapsed time
    return walk_node_pooled(available, graph, worker_pool, elapsed + worker_pool.elapsed())


def is_available(node, graph):
    # A node is deemed "available" if it doesn't exist as a child to any other node
    for v in graph.values():
        if node in v:
            return False
    return True


def instruction_duration(instruction):
    return ord(instruction) - 64


class TimedInstruction:
    def __init__(self, instruction, duration):
        self.instruction = instruction
        self.duration = duration

    def __repr__(self):
        return f"{self.instruction} for {self.duration}"

    def __eq__(self, other):
        return self.instruction == other.instruction

    def __lt__(self, other):
        return self.instruction < other.instruction

    def __gt__(self, other):
        return self.instruction > other.instruction

    def __hash__(self):
        return ord(self.instruction)

    @classmethod
    def from_instruction(cls, instruction, base_time=0):
        return cls(instruction, base_time + instruction_duration(instruction))

    def tick(self):
        self.duration -= 1

    def done(self):
        return not bool(self.duration)


class WorkerPool:
    def __init__(self, size):
        self._pool = {k: None for k in range(size)}
        self._elapsed = 0

    def elapsed(self):
        return self._elapsed

    def is_assignable(self, instruction):
        # Instructions already assigned to a worker cannot be assigned again
        for worker_id, assigned in self._pool.items():
            if assigned and assigned == instruction:
                return False
        return True

    def assign(self, instruction):
        # Assign the instruction to the next available worker, if one exists
        for worker_id, assignment in self._pool.items():
            if not assignment:
                self._pool[worker_id] = instruction
                return

    def tick(self):
        self._elapsed = 0
        completed = []
        while len(completed) == 0:
            self._elapsed += 1
            for worker_id, assignment in self._pool.items():
                # Skip workers with no assignment
                if not assignment:
                    continue
                assignment.tick()
                if assignment.done():
                    # Put worker's instruction into the completed list and make the worker available again
                    completed.append(assignment)
                    self._pool[worker_id] = None

        return completed
