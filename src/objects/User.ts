enum UserType {
    CSH,
    GOOGLE
}

interface User {
    id: string, // CSH Username
    user_type: UserType, // CSH or Google
    first_name: string,
    last_name: string,
    picture: string,
    admin: boolean,
    email: string
}

export default User