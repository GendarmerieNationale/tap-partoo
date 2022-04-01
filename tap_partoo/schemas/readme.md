Specify [json-schema](https://json-schema.org/) of the API data, in a .json file for each stream.

# Helpful tools
- https://jsonschema.net/home
  - Given an example of a json response, generate a json schema that matches. 
  - To obtain a simplified json schema with only required fields, you can:
    - uncheck all keywords except `type`
    - use `First (single schema)` for array validation
    - use `None` for Identifier Type
  - Optionally, you can 
    - manually specify `format`
    - manually allow for null values, e.g. `"type": ["null", "string"]`
- https://www.jsonschemavalidator.net/
  - Check that your schema matches specific examples

# Partoo Implementation
> Note: the full API specification can be downloaded [here](https://developers.partoo.co/a0346514-4cd1-4ef8-9660-ce4c12291826)

Responses from the [Partoo API](https://developers.partoo.co/rest_api/v2/#tag/Businesses) have the following format:
```
{
"page": 1,
"max_page": 10,
"count": 287,
"businesses": [
    {
      "id": ...,
      "name": ...
      etc
    },
    {...}
  ]
}
```
And we only read the data inside `businesses` (in the `Stream.parse_response` method), so this is what the json schema should specify directly (not `page`, `max_page`, etc).
