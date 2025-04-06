import React, {useState, useEffect} from "react";
import '../../css/games/gamelist.css';
import '../../index.tsx.css';
import Game from "../../objects/Game";
import GameCard from "./GameCard";

const GameList: React.FunctionComponent = () => {
    let [gameList, setGameList] = useState([]);

    const loadGameList = async () => {
        try {
            let response = await fetch('https://devcade.csh.rit.edu/api/games/');
            //let response = await fetch('games.json');
            let gameList = response.json();
            console.log(gameList);
            gameList.then(value => setGameList(value));
        }
        catch (err) {
            console.log(err);
        }
        
    }

    useEffect(() => {
        loadGameList();
    }, []);

    if (Object.keys(gameList).length === 0) {
        return <div id="game-grid">
        </div>
    }

    return (
        <div id="game-grid">
            {gameList.map(
                (g:Game) => <GameCard 
                id={g.id} 
                author={g.author}
                upload_date={g.upload_date}
                name={g.name}
                hash={g.hash}
                description={g.description}
                tags={g.tags}
                user={g.user}
                />
                )}
        </div>
    )
}

export default GameList