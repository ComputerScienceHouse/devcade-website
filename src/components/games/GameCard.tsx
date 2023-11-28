import React from "react";
import axios from "axios";

function getGameData(game: Game) {
    axios.get(`https://devcade.csh.rit.edu/api/game/${game.id}`);
}
const GameCard: React.FunctionComponent = () => {
    return (
        <div></div>
    )
}