import Tag from "./Tag"
import User from "./User"

interface Game {
    id: string,
    author: string,
    upload_date: Date,
    name: String,
    hash: String,
    description: String,
    tags: Tag[]
    user: User
}

export default Game