import React from "react";
import '../../css/homegrid.css';
import '../../index.tsx.css';
import { Button, CardLink } from "reactstrap";
import { Link } from "react-router-dom";

const CreditsButton: React.FunctionComponent = () => {

    return (
        <Link className="creditsbutton" to="/credits">
            Credits
        </Link>
    )
}

export default CreditsButton