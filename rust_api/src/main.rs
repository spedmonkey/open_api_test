use reqwest::Error;

#[tokio::main]
async fn main() -> Result<(), Error> {
    // Define the API endpoint
    let url = "http://127.0.0.1:5000/hello/";

    // Send a GET request to the API
    let response = reqwest::get(url).await?;

    // Check if the request was successful
    if response.status().is_success() {
        // Parse the JSON response
        let data: serde_json::Value = response.json().await?;
        // Print the response
        println!("Response from API: {}", data);
    } else {
        println!("Failed to retrieve data from API. Status code: {}", response.status());
    }

    Ok(())
}