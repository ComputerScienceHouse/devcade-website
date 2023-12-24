import { useOidcAccessToken, useOidc, useOidcIdToken } from '@axa-fr/react-oidc'
import UserInfo from '../objects/UserInfo'
import HomeGrid from '../components/home/HomeGrid'

const Home = () => {
    // // important hooks
    // const { accessTokenPayload } = useOidcAccessToken()   // this contains the user info in raw json format
    // const userInfo = accessTokenPayload as UserInfo       // 
    // const { idToken, idTokenPayload } = useOidcIdToken()  // this is how you get the users id token
    // const { login, logout, isAuthenticated } = useOidc()  // this gets the functions to login and logout and the logout state

    return (
        <>
            <HomeGrid />
        </>
    )
}

export default Home