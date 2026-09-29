# 余弦相似度

# 1.计算点积
def dot_product(v1: list[float], v2: list[float]) -> float:
    return sum(x * y for x, y in zip(v1, v2))


# 2.计算向量的模
def vector_magnitude(vector: list[float]) -> float:
    return sum(x ** 2 for x in vector) ** 0.5


# 3.计算余弦相似度
def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    return dot_product(v1, v2) / (vector_magnitude(v1) * vector_magnitude(v2))


# 实例
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
similarity = cosine_similarity(vector1, vector2)
print(similarity)
