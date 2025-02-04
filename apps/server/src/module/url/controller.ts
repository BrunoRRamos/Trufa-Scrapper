import { Request, Response } from "express";
import { addUrl, getAllUrls } from "./service";
import { HttpCodes } from "../../helpers/HttpCodes";
import { UrlDTO } from "../../types/dtos";

export async function handleCreate(req: Request, res: Response): Promise<Response<UrlDTO>> {
    const inputData = req.body;
    const newUrl = await addUrl(inputData);
    return res.status(HttpCodes.OK).json(newUrl);
}

export async function handleGetAll(req: Request, res: Response): Promise<Response<UrlDTO[]>> {
    const allUrl = await getAllUrls();
    return res.status(HttpCodes.OK).json(allUrl);
}