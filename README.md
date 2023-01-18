# Polls API

## Install the command line client
$ pip install coreapi-cli
login
create
POST /login/
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action login create
polls
list
GET /polls/
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls list
list_0
GET /polls/
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls list_0
create
POST /polls/
Request Body
The request body should be a "application/json" encoded object, containing the following items.

Parameter	Description
question required	
created_by required	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls create -p question=... -p created_by=...
create_0
POST /polls/
Request Body
The request body should be a "application/json" encoded object, containing the following items.

Parameter	Description
question required	
created_by required	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls create_0 -p question=... -p created_by=...
read
GET /polls/{id}/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	A unique integer value identifying this poll.
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls read -p id=...
read_0
GET /polls/{id}/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	A unique integer value identifying this poll.
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls read_0 -p id=...
update
PUT /polls/{id}/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	A unique integer value identifying this poll.
Request Body
The request body should be a "application/json" encoded object, containing the following items.

Parameter	Description
question required	
created_by required	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls update -p id=... -p question=... -p created_by=...
partial_update
PATCH /polls/{id}/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	A unique integer value identifying this poll.
Request Body
The request body should be a "application/json" encoded object, containing the following items.

Parameter	Description
question	
created_by	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls partial_update -p id=... -p question=... -p created_by=...
delete
DELETE /polls/{id}/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	A unique integer value identifying this poll.
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls delete -p id=...
delete_0
DELETE /polls/{id}/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	A unique integer value identifying this poll.
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls delete_0 -p id=...
choices > list
GET /polls/{id}/choices/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls choices list -p id=...
choices > create
POST /polls/{id}/choices/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	
Request Body
The request body should be a "application/json" encoded object, containing the following items.

Parameter	Description
votes	
choice_text required	
poll required	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls choices create -p id=... -p votes=... -p choice_text=... -p poll=...
choices > vote > create
POST /polls/{id}/choices/{choice_pk}/vote/
Path Parameters
The following parameters should be included in the URL path.

Parameter	Description
id required	
choice_pk required	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action polls choices vote create -p id=... -p choice_pk=...
swagger-docs
list
GET /swagger-docs/
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action swagger-docs list
users
create
POST /users/
Request Body
The request body should be a "application/json" encoded object, containing the following items.

Parameter	Description
username required	Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
email	
password required	
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action users create -p username=... -p email=... -p pas
