def generate_brackets(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)

    return result



assert generate_brackets(1) == ["()"]

assert set(generate_brackets(2)) == {
    "(())",
    "()()"
}

assert len(generate_brackets(3)) == 5

print(generate_brackets(3))
print("Автотест пройшов успішно")