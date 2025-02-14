import axios from 'axios'

const baseAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v2/',
})

export { baseAPI }
