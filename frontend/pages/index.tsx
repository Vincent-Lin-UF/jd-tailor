import { useEffect, useState } from "react";

export default function Home() {
    const [status, setStatus] = useState<string>("checking...")

    useEffect(() => {
        fetch("http://localhost:8000/health")
            .then((r) => r.json())
            .then((j) => setStatus(j.status ?? "unknown"))
            .catch(() => setStatus("Backend is not reachable"));
    }, []);

    return (
        <main style={{padding : 24, fontFamily: "ui-sans-serif, system-ui"}}>
            <h1>JD-Grounded Resume Tailor</h1>
            <p>Backend Health: <b>{status}</b></p>
            <p>Stuff Stuff This is a paragraph.</p>
        </main>
    );
}