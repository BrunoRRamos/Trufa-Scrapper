import { Request, Response, json } from "express";
import urlRouter from "../module/url/routes";

const routes = (app: any) => {
  app.get('/', (req: Request, res: Response) => {
    res.send('batata');
  });

  app
  .use(json())
  .use("/url", urlRouter)
};

export default routes;