def paginate(data, page, size):
    """Returns a paginated portion of sample data"""
    start = (page -1) * size # calculate starting index
    end = start + size # calculate ending index
    return data[start:end]

# sample data(list of 100 nums)
data = list(range(1, 101)) # [1, 2, 3,..., 100]

# get page 2, with 10 items per page
page = 2
size = 10
result = paginate(data, page, size)

print(result)