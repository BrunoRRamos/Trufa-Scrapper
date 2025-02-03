import { Request, Response } from "express";

const routes = (app: any) => {
  app.get('/', (req: Request, res: Response) => {
    res.send('batata');
  });
};

export default routes;