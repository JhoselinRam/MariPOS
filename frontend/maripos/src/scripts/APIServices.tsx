const API = process.env.REACT_APP_BACKEND;

export interface response{
    status:number
    body:object
}

export async function getUsers(): Promise<response> {
    const data = await fetch(`${API}/users`);
    const apiResponse = await data.json();
    return apiResponse;
}