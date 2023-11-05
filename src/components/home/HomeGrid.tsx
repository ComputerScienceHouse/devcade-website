import React from "react";
import '../../css/homegrid.css';
import '../../index.tsx.css';
import DevcadeProject from "./DevcadeProject";
import DevcadeTeam from "./DevcadeTeam";
import CSH from "./CSH";

const HomeGrid: React.FunctionComponent = () => {

    return (
        <div className="bg">
            <div className="grid">
                <DevcadeProject />
                <DevcadeTeam />
                <CSH />
            </div>
        </div>
    )
}

export default HomeGrid