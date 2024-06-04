Add-Type -AssemblyName "System.Net.Http"
$uri = "http://localhost:8888/score"
$filePath = "data\score.csv"

$multipartContent = [System.Net.Http.MultipartFormDataContent]::new()
$fileStream = [System.IO.File]::OpenRead($filePath)
$fileContent = [System.Net.Http.StreamContent]::new($fileStream)
$fileContent.Headers.ContentType = [System.Net.Http.Headers.MediaTypeHeaderValue]::new("text/csv")
$multipartContent.Add($fileContent, "file", [System.IO.Path]::GetFileName($filePath))

$client = [System.Net.Http.HttpClient]::new()
$response = $client.PostAsync($uri, $multipartContent).Result

$response.Content.ReadAsStringAsync().Result
