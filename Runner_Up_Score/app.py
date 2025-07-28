if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    matrix=list(arr)
    max_score=max(matrix)
    filtered_score=[score for score in matrix if score!=max_score]
    print(max(filtered_score))
