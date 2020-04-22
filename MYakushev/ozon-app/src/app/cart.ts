import {Product, Products} from './product';


export class Cart {
  countProducts: number;
  id: number;
  is_checkout: boolean;
  purchase: Products[];
  totalPrice: number;
  totalWeight: number;
}
