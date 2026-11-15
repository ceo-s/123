def mean_score(scores: list[float]) -> float:
    """Возвращает среднее значение списка оценок."""
    if not scores:
        raise ValueError("Список оценок не должен быть пустым")
    return sum(scores) / len(scores)


if __name__ == "__main__":
    print(mean_score([4, 5, 3, 5]))
