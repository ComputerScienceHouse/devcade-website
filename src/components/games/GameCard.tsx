import React from "react";
import axios from "axios";
import Game from "../../objects/Game";

function getGameData(game: Game) {
    let data = axios.get(`https://devcade.csh.rit.edu/api/game/${game.id}/`);
}
const GameCard: React.FunctionComponent = () => {
    return (
        <div></div>
    )
}
export default GameCard