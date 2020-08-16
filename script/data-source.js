class DataSource {
    static searchData(keyword) {
        return fetch(`http://185.201.9.138:7070/search-shop?q=${keyword}`, {
            credentials: 'same-origin',
        })
        .then(response => response.json())
        .then(responseJson => {
            if (responseJson.shops) {
                return Promise.resolve(responseJson.shops);
            } else {
                return Promise.reject(`${keyword} is not found`)
            }
        })
    }
}

export default DataSource;
