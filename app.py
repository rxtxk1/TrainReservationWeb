from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize seats
seats = [[0] * 7 for _ in range(11)] + [[0] * 3]

# Display the seating layout as HTML
@app.route("/")
def home():
    return render_template("index.html", seats=seats)

# Handle seat booking
@app.route("/book", methods=["POST"])
def book():
    num_seats = int(request.form.get("num_seats"))
    booked_seats = []

    for i, row in enumerate(seats):
        available = [j for j, seat in enumerate(row) if seat == 0]
        if len(available) >= num_seats:
            for k in range(num_seats):
                row[available[k]] = 1
                booked_seats.append((i + 1, available[k] + 1))
            break

    if not booked_seats:
        return "Not enough seats available!", 400

    return render_template("index.html", seats=seats, message=f"Seats booked: {booked_seats}")

if __name__ == "__main__":
    app.run(debug=True)
