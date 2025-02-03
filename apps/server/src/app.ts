import express from "express";
import routes from "./routes/index.ts";
import db from "./config/dbConnect.ts";

db.on("error", console.log.bind(console, "Erro de conexão"));
db.once("open", () => {
    console.log("Connected to DataBase")
});

const app = express();

routes(app);

export default app;
