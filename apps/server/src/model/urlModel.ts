import { randomUUID } from "crypto";
import mongoose from "mongoose";

const urlSchema = new mongoose.Schema({
    id: { type: String, default: () => randomUUID() },
    name: { type: String, required: true },
    url: { type: String, required: true, unique: true }
});

const url = mongoose.model("url", urlSchema);

export default url;