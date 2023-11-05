import React from "react";
import '../../css/homegrid.css';
import '../../index.tsx.css';

const DevcadeProject: React.FunctionComponent = () => {

    return (
        <div className="devcadeproj-box">
            <h2 className="devcadeproj-header">What is Devcade?</h2>
            <p className="devcadeproj-info">
                Devcade is a fully custom arcade machine made by members at RIT's
                <a className="bodylink" href="https://csh.rit.edu"> Computer Science House</a>.
                Devcade is an arcade built for developers, by developers. The arcade cabinet, software, and
                games for Devcade were mainly built during the Fall 2022 semester and the project is still
                being maintained and updated.
            </p>

            <p className="devcadeproj-info">
                The arcade cabinet was first shown off at the 2022 <a className="bodylink" href="https://rochester.makerfaire.com">Rochester Makerfaire </a>
                and the 2023 <a className="bodylink" href="https://rit.edu/imagine">ImagineRIT festival</a>. The next exhibition of Devcade will
                be at ImagineRIT 2024. This cabinet is the first of its kind, but hopefully not the last.
            </p>

            <img className="devcade-img" src="./img/cabinetirl.png" />
        </div>
    )
}

export default DevcadeProject