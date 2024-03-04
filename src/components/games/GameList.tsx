import React from "react";
import axios from "axios";
import '../../css/games/gamelist.css';
import '../../index.tsx.css';

function getGameList() {
    let gameList = axios.get('https://devcade.csh.rit.edu/api/games/');
    console.log(gameList);
}

const GameList: React.FunctionComponent = () => {
    let res = getGameList();

    return (

        <div id="game-grid">
        </div>
    )
}

export default GameList