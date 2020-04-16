import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Product} from '../product';
import {ProductService} from "../product.service";
import {Observable, Subject} from "rxjs";

@Component({
  selector: 'app-page-search',
  templateUrl: './page-search.component.html',
  styleUrls: ['./page-search.component.css']
})
export class PageSearchComponent implements OnInit {
  productsOnPage$: Product[] = [];
  private searchTerms = new Subject<string>();
  nameSearch: string;
  toggleSearchInfo = false;

  constructor(private productService: ProductService) {
  }
  showSearchItems($event: string) {
    this.searchTerms.next($event);
    this.nameSearch = $event;
    this.productService.searchProducts($event).subscribe(value => {
      this.productsOnPage$ = value;
      this.toggleSearchInfo = true;
    });
  }
  ngOnInit(): void {
  }
}
