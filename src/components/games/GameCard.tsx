import React from "react";
import Game from "../../objects/Game";



const GameCard = ({id, author, upload_date, name, hash, description, tags, user}: Game):JSX.Element => {
    return (
        <div id={`game-${id}`} className="game-card">
            <h2>{`${name} - ${author}`}</h2>
            <p>{description}</p>
        </div>
    )
}
export default GameCard