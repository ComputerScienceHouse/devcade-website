interface Game {
    id: string,
    author: string,
    upload_date: Date,
    name: String,
    hash: String,
    description: String,
    tags: Tag[]
    user: User
};