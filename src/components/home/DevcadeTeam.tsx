import React from "react";
import '../../css/homegrid.css';
import '../../index.tsx.css';
import CreditsButton from "./CreditsButton";

const DevcadeTeam: React.FunctionComponent = () => {

    return (
        <div className="devcadeteam-box">
            <h2 className="devcadeteam-header">Who are we?</h2>

            <p className="devcadeteam-info">
                Devcade is being actively developed by a group of students at RIT's Computer Science House.
            </p>

            <p className="devcadeteam-info">
                The Devcade project is led by <a className="bodylink" href="https://noahemke.com">Noah Emke</a>,
                a fourth year Game Design and Development major at RIT. Noah leads a team of about a dozen CSH
                members, ranging from first years to fifth years. Many of these team members are making their
                own games for the cabinet, some are working on the backend API and databases, some on the onboard
                software, and some on the physical design of the cabinet itself -- there's something for everyone
                on this project.
            </p>
            
            <CreditsButton />
        </div>
    )
}

export default DevcadeTeam