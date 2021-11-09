def solution(sizes):
    sizes=[sorted(size,reverse=True) for size in sizes]

    return max([size[0] for size in sizes]) * max([size[1] for size in sizes])