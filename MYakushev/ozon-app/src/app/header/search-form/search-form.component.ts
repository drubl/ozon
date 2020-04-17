import {Component, OnInit, Output, EventEmitter} from '@angular/core';
import {Observable, Subject} from 'rxjs';
import {ProductService, SearchProducts} from '../../product.service';
import {Product} from '../../product';
import { debounceTime, distinctUntilChanged, switchMap} from 'rxjs/operators';
import {Router} from "@angular/router";
import {Auth} from "../../auth";


@Component({
  selector: 'app-search-form',
  templateUrl: './search-form.component.html',
  styleUrls: ['./search-form.component.css']
})
export class SearchFormComponent implements OnInit {
  @Output() onClickSearchButton: EventEmitter<string> = new EventEmitter<string>();
  products$: Observable<Product[]>;
  private searchTerms = new Subject<string>();
  constructor(public productService: ProductService, private router: Router, private auth: Auth) { }

  search(title: string): void {
    this.searchTerms.next(title);
  }
  ngOnInit(): void {
    this.products$ = this.searchTerms.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap((title: string) => this.productService.searchProducts(title)),
    );
  }


  searchButtonClick($event: Event, value: string, searchBox: HTMLInputElement) {
    $event.preventDefault();

    this.router.navigate([`products?search=${$event}`]);
    this.onClickSearchButton.emit(value);
    searchBox.value = '';
  }
}
