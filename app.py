from flask import Flask, render_template

app = Flask(__name__)

MATRIX_A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

MATRIX_B = [
    [26, 27, 28],
    [29, 30, 31],
    [32, 33, 34],
    [35, 36, 37],
    [38, 39, 40],
]

NAME = "Earl John B. Viray"


def multiply_row(row_index):
    row_result = [0] * 3
    for j in range(3):
        for k in range(5):
            row_result[j] += MATRIX_A[row_index][k] * MATRIX_B[k][j]
    return row_result


RESULT_MATRIX = [multiply_row(i) for i in range(5)]


@app.route('/')
def index():
    return render_template(
        'index.html',
        matrix_a=MATRIX_A,
        matrix_b=MATRIX_B,
        result_matrix=RESULT_MATRIX,
        name=NAME,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
