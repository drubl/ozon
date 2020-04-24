import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Product} from '../../product';
import {ProductService} from '../page-product/services/product.service';
import {Observable, Subject, Subscription} from 'rxjs';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-page-search',
  templateUrl: './page-search.component.html',
  styleUrls: ['./page-search.component.css']
})
export class PageSearchComponent implements OnInit {

  productsOnPage: Product[] = [];
  private searchTerms = new Subject<string>();
  nameSearch: string;
  toggleSearchInfo = false;

  constructor(private productService: ProductService, private route: ActivatedRoute) {
  }
  ngOnInit(): void {

  }

  showSearchItems($event: string) {
    this.searchTerms.next($event);
    this.nameSearch = $event;
    this.productService.searchProducts($event).subscribe(value => {
      this.productsOnPage = value;
      this.toggleSearchInfo = true;
    });
  }

  addProductToCart(id: number) {
    this.productService.addProduct(id).subscribe(answer => {
      console.log(answer);
    });
  }

}
