"use client"
import { useRouter } from "next/navigation"
import { useEffect, useState } from "react";

function AuthWrapper(WrapperComponent: any) {
    const Wrapper = (props: any) => {
        const router = useRouter();
        const [loading, setLoading] = useState(true);
        const [loggedIn, setLoggedIn] = useState(false);
        const [sessionExpired, setSessionExpired] = useState(false);
        const [accessDenied, setAccessDenied] = useState(false);


        useEffect(() => {
            const verifyToken = async () => {
                try {
                    const res = await fetch('http://localhost:5000/api/v1/auth/verify', {
                        method: 'POST',
                        credentials: 'include',
                    });
                    if (res.ok) {
                        setLoggedIn(true);
                        setLoading(false);
                    } else if (res.status === 403) {
                        router.push('/auth/signin');
                    } else if (res.status === 401) {
                        setLoading(false);
                        setSessionExpired(true);
                    } else {
                        setLoading(false);
                        setAccessDenied(true);
                    }
                } catch (error) {
                    setAccessDenied(true);
                    setLoading(false);
                    router.push("/auth/access")
                }
            };

            verifyToken();
        }, []);

        const extendAccessToken = async () => {
            try {
                const res = await fetch(
                    'http://localhost:5000/api/v1/auth/refresh_token',
                    {
                        method: 'POST',
                        credentials: 'include',
                    },
                );
                if (res.ok) {
                    setLoggedIn(true);
                    console.log("HATA");
                    setTimeout(() => {
                        window.location.reload();
                    }, 1500);
                } else {
                    console.log('Error extending access token');
                }
            } catch (error) {
                console.log('Error extending access token', error);
            }
        };

        const handleLogout = async () => {
            try {
                const res = await fetch('http://localhost:5000/api/v1/auth/logout', {
                    method: 'POST',
                    credentials: 'include',
                });
                if (res.ok) {
                    localStorage.clear();
                    console.log('Çıkış Başarılı');
                    router.push('/auth/signin');
                }
            } catch (err) {
                router.push('/auth/signin');
                console.log(err);
            }
        };

        if (loading) {
            return (
                <h1>Loading...</h1>
            );
        }

        if (accessDenied) {
            return (
                <section>
                    Access Denied
                </section>
            )
        }

        if (sessionExpired) {
            return (
                <section>
                    Sorry, session has expired
                </section>
            )
        }

        return (
            <section>
                <WrapperComponent loggedIn={loggedIn} {...props} />
            </section>
        )


    }
    return Wrapper;
}

export default AuthWrapper;