# Error Codes and Messages

## HTTP Status Codes
- `400` - Bad Request (invalid input)
- `401` - Unauthorized (authentication required)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found (resource not found)
- `422` - Unprocessable Entity (validation failed)
- `500` - Internal Server Error (server error)
- `503` - Service Unavailable (service temporarily unavailable)

## Specific Error Messages

### Search Errors
- `400` - "Limit must be greater than 0"
- `400` - "Limit must be positive"
- `400` - "Limit exceeds maximum of 100"
- `400` - "Invalid search query format"
- `404` - "No methods found matching criteria"

### Indexing Errors
- `400` - "Invalid file path provided"
- `400` - "Unsupported file type"
- `422` - "Database schema validation failed"
- `500` - "Failed to parse C# file"

### MCP API Errors
- `400` - "Invalid request format"
- `400` - "Missing required parameters"
- `401` - "Authentication required"
- `404` - "Method not found"
- `500` - "MCP server error"

### Diff Errors
- `400` - "Invalid database path"
- `404` - "Database file not found"
- `422` - "Database schema mismatch"
- `500` - "Failed to compare databases"

### Report Errors
- `400` - "Invalid report type"
- `400` - "Invalid date range"
- `404` - "No data available for report"
- `500` - "Failed to generate report"

### Tag Hierarchy Errors
- `400` - "Invalid tag relationship"
- `400` - "Circular dependency detected"
- `422` - "Tag hierarchy validation failed"
- `500` - "Failed to process tag hierarchy"

## Error Response Format

Следует RFC 7807 "Problem Details for HTTP APIs" (https://tools.ietf.org/html/rfc7807)

```json
{
  "type": "https://testkitdex.com/errors/invalid-request",
  "title": "Invalid Request",
  "status": 400,
  "detail": "Invalid request format",
  "instance": "/api/v1/search",
  "timestamp": "2024-01-01T12:00:00Z",
  "code": "INVALID_REQUEST_FORMAT"
}
``` 