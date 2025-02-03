import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/',
})

export { getAPI }
