
//Main Door to heaven.
const apiUrl = "{{host.url}}/api/users";

// Function to fetch data from the API
async function fetchData() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        console.log("Data from API:", data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Function to post data to the API
async function postData(data) {

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const responseData = await response.json();
        console.log("Response from API:", responseData);
    } catch (error) {
        console.error("Error posting data:", error);
    }
}

// Function to update data in the API
async function updateData(id, newData) {
    try {
        const response = await fetch(${apiUrl}/${id}, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newData)
        });
        const responseData = await response.json();
        console.log("Response from API:", responseData);
    } catch (error) {
        console.error("Error updating data:", error);
    }
}

// Function to delete data from the API
async function deleteData(id) {
    try {
        const response = await fetch(${apiUrl}/${id}, {
            method: 'DELETE'
        });
        const responseData = await response.json();
        console.log("Response from API:", responseData);
    } catch (error) {
        console.error("Error deleting data:", error);
    }
}