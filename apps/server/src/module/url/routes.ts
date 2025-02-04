import { Router } from "express";
import { handleCreate, handleGetAll } from "./controller";

const urlRouter = Router();

urlRouter
    .post("/", (request, response) => {
        return handleCreate(request, response);
    })
    .get("/", (request, response) =>{
        return handleGetAll(request, response);
    })

export default urlRouter;