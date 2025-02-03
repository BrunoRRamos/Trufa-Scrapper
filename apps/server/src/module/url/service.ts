import url from "../../model/urlModel";
import { IUrl, UrlDTO } from "../../types/dtos";

export async function addUrl(data: UrlDTO): Promise<IUrl> {
    return await url.create(data);
}

export async function getAllUrls(): Promise<IUrl[]> {
    return await url.find();
}

export async function deleteUrl(id: String): Promise<IUrl> {
    return url.findByIdAndDelete(id);
}