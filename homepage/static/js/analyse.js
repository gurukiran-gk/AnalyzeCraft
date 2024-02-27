const functions = ['head', 'tail', 'function3', 'function4', 'function5'];

    // Get references to elements
    const searchBox = document.getElementById('searchBox');
    const functionResults = document.getElementById('functionResults');
    const inputPopup = document.getElementById('inputPopup');
    const functionInput = document.getElementById('functionInput');

    // Add event listener to the search box
    searchBox.addEventListener('input', function() {
        const searchValue = this.value.toLowerCase();
        const filteredFunctions = functions.filter(func => func.toLowerCase().includes(searchValue));
        displayFilteredFunctions(filteredFunctions);
    });

    // Function to display filtered functions
    function displayFilteredFunctions(filteredFunctions) {
        // Clear previous results
        functionResults.innerHTML = '';
        // Add filtered functions to the list
        filteredFunctions.forEach(func => {
            const listItem = document.createElement('a');
            listItem.textContent = func;
            listItem.style.cursor = 'pointer';
            listItem.addEventListener('click', function() {
                showFunctionInputPopup(func);
            });
            functionResults.appendChild(listItem);
        });
        // Display the dropdown
        functionResults.style.display = filteredFunctions.length ? 'block' : 'none';
    }

    // Function to show popup for function input
    function showFunctionInputPopup(func) {
        functionInput.value = ''; // Clear previous input
        inputPopup.style.display = 'block';
        functionResults.style.display = 'none'; // Hide search results when input popup is displayed
    }

    // Function to close the input popup
    function closeInputPopup() {
        inputPopup.style.display = 'none';
    }

    // Function to submit function input
    function submitFunctionInput() {
        const input = functionInput.value;
        alert('Input for function: ' + input); // Replace with your custom logic
        closeInputPopup();
    }

    // Close the input popup when clicking outside of it or the search box
    window.addEventListener('click', function(event) {
        if (event.target !== searchBox && event.target !== functionResults) {
            functionResults.style.display = 'none';
        }
    });