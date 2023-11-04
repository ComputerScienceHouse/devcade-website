import React from "react"
import { Container } from "reactstrap"
import NavBar from "../components/NavBar"

type Props = {
    children: React.ReactNode
}

export const PageContainer: React.FC<Props> = ({ children }) => {
    return (
        <div>
            <NavBar />
            <div>{children}</div>
        </div >
    )
}

export default PageContainer