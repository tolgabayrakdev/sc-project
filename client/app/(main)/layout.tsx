'use client'
import Layout from '../../layout/layout';
import AuthWrapper from '../../util/auth-wrapper';



interface AppLayoutProps {
    children: React.ReactNode;
}


function AppLayout({ children }: AppLayoutProps) {
    return <Layout>{children}</Layout>;
}


export default AuthWrapper(AppLayout);