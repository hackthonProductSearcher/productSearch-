import DataSource from "./data-source.js";

const datasearch = () => {
    const searchDataElement = document.querySelector(".search-data");
    const submitDataElement = document.querySelector(".submit-data");
    const dataContainerElement = document.querySelector(".data-container");

    const onButtonSearchClicked = () => {
        DataSource.searchData(searchDataElement.value)
        .then(renderResult)
        .catch(fallbackResult)
    };

    const renderResult = results => {
        dataContainerElement.innerHTML = "";
        results.forEach(data => {
            const {strMeal, strArea} = data;
            const dataElement = document.createElement("div");
            dataElement.setAttribute("class", "data");

            dataElement.innerHTML = `
                <h3>${strMeal}</h3>
                <h4>${strArea}</h4>
                `;
            
            dataContainerElement.appendChild(dataElement);
        })
    };

    const fallbackResult = message => {
        dataContainerElement.innerHTML = "";
        dataContainerElement.innerHTML += `<h2>${message}</h2>`;
    };

    submitDataElement.addEventListener("click", onButtonSearchClicked);
}

export default datasearch;
