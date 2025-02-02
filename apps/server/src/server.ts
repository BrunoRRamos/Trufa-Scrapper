import express, { Request, Response } from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

mongoose.set("strictQuery", true);
mongoose.connect(process.env.MONGO_URI!)
  .then(() => console.log('Connected to MongoDB Atlas !'))
  .catch((err) => console.error('MongoDB connection error:', err));

app.get('/', (req: Request, res: Response) => {
  res.send('batata');
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});