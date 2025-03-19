from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (100 items)
data = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]

@app.route("/items", methods=["GET"])
def get_items():
    # Get page and size from query parameters (default: page=1, size=10)
    page = int(request.args.get("page", 1))
    size = int(request.args.get("size", 10))

    # Validate page and size
    if page < 1 or size < 1:
        return jsonify({"error": "Page and size must be positive integers"}), 400

    # Calculate start and end index
    start = (page - 1) * size
    end = start + size

    # Paginate data
    paginated_data = data[start:end]

    # Metadata
    response = {
        "total_items": len(data),
        "total_pages": (len(data) + size - 1) // size,
        "current_page": page,
        "page_size": size,
        "data": paginated_data
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)  # Run with: python filename.py
