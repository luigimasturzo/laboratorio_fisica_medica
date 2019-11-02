//
// Author: E.Gorini (email: edoardo.gorini@le.infn.it)
// Lastt modification 20/4/2018
//
// This Macro fits a function with info contained in a text file (i.e. nomefile.txt)
// and plots the graph and the pulls in the chosen range. 
// It produces a .png output of the plot in the same folder of the text file
// the .png file can be added to a google doc in a simple way
// Optionally one can plot only the graph, define a range for fitting and plotting or zoom
// Macro automatically detects if there is a large range in x variable and set log scale in case
//
// First argument is a string variable which contains the name of txt file with information to be plotted (without extension)
// Second argument is a boolean variable (false,true), which enable or not the plotting of the pulls (default=true)
// Third argument is real variable (default=0) which defines the lower fitting range
// Fourth argument is real variable (default=100) which defines the upper fitting range
// Fifth argument is a boolean variable (false,true), which enable or not the zooming of the plots in the defined range (default=false)
// 
// as usual, the arguments can be omitted when they default to something. 
//
//   example usage:
// Plots and Fit the data contained in nomefile (extension type .txt) and plot also the pulls
//   [0] .x LinFit.C("nomefile"); 
// or, to not plot the pulls
//   [0] .x LinFit.C("nomefile",false); 
// or, to plot the pulls and set the minimum of the x axis range for fitting
//   [0] .x LinFit.C("nomefile",true,0.0)
// or, to not plot the pulls and to set a range (min,max) for fitting
//   [0] .x LinFit.C("nomefile",false,1.0,10.0)
// or, plot the pulls, set a range (1.0,10) for fitting and plot only in the fitted range
//   [0] .x LinFit.C("nomefile",true,1.0,10.0,true)
//
// 
// the txt file should have the following format: 
// info lines should always start with "# " followed by some info
// data lines are normally without "# "
// CAUTION: first data line should contain single spaces or single tabs between numbers  
// data lines format should be x,y,deltax,deltay OR x,y,deltay OR x,y	 					
// data points can be temporarily removed just adding "# " at the start of the line (line starting with 2.226 is an example)
/* All the following lines (from # until 0.09) could be put in a nomefile.txt and make a valid starting working file
# Titolo del Plot
# Legenda asse x [unita']
# Legenda asse y [unita']
# nomeparametro1 nomeparametro2
4.043	14.000	0.002	0.05
3.573	13.000	0.002	0.05
3.121	12.000	0.003	0.05
2.670	11.000	0.002	0.05
# 2.226	  10.000	0.002	0.05
1.773	9.000	0.002	0.05
1.335	8.000	0.003	0.05
0.927	7.000	0.002	0.05
0.485	6.000	0.003	0.09
*/
// 
//
#include <algorithm>
//
void LinFit(string file, bool makepulls=true, float min=0, float max=100, bool zoom = false){

// ROOT initialization
  gROOT->Reset();
// graphic   
  gStyle->SetTitleStyle(0);
  gStyle->SetTitleBorderSize(0);
  gStyle->SetTitleX(0.3);
  gStyle->SetTitleY(1.0);
  gStyle->SetTitleH(.1);
  gStyle->SetTitleW(.83);
  if(makepulls)gStyle->SetMarkerSize(0.8);

// print statistics if true, write output file if true 
  bool makestat=true; bool output=true; 
// set the number of decades found to set log scale on x. To be done also for y scale
  const int maxdec=3;  
// 
  if (makestat) {
	gStyle->SetOptStat(1);
	gStyle->SetOptFit(111111);
  }
  
// here opens the data file, should be a text file, extension .txt (made with WordPad on Windows)
// first check if the extension is txt, if not assumes is a txt file
  if(file.substr(file.length()-4,file.length())!=".txt")file=file+".txt";
  
  ifstream in;
  in.open(file.c_str());
// get out if file do not exists.. 
  if(in.is_open()==0){
     in.close();
     gROOT->Reset();
    cout << "File " << file <<" do not exist, exit\n";
    return;
  }
//   
// File exists, start reading the info part
// reads plot title and X and Y labels
  string Title,Xtitle,Ytitle;
  getline(in,Title);  Title=Title.substr(2,Title.length());
  getline(in,Xtitle); Xtitle=Xtitle.substr(2,Xtitle.length());
  getline(in,Ytitle); Ytitle=Ytitle.substr(2,Ytitle.length());
  cout << "\n\tPlot Title is: "<< Title <<"\n";
  cout << "\tx axis title is: "<< Xtitle <<"\n";
  cout << "\ty axis title is: "<< Ytitle <<"\n";
  

// Define a linear function
  string Function="[0]+[1]*x";
  
// easter egg for constant line. If title contains COSTANTE in the first 8 character
// the fit is performed with a constant line and the text  COSTANTE is removed from Title.    
  if(Title.substr(0,8)=="COSTANTE"){
    Title=Title.substr(9,Title.length());
    Function="[0]";
  } 
  cout << "\tFunction to fit is: "<< Function << "\n";
// create the funzione function to be fitted
  TF1 *funzione = new TF1("funzione",Function.c_str(),min,max);
// reads and sets number of parameters of function       
  Int_t numpar=funzione->GetNpar(); 

  cout << "\tNumber of Parameters is: "<< numpar;

// reads parameter names       
  vector<string> parnames;
  TString buff; 
  in >> buff; 
  if(buff=="#"){
    for (int np=0;np<numpar;np++){
      string sbuf;
      in >> sbuf;
      parnames.push_back(sbuf);
    }
  } else cout << "Parameter names not found exit\n";
  
  cout << "\n\tParameter names are: ";
  for (int np=0;np<numpar;np++)cout << parnames[np] << " ";
    
// code to identify type of data
// read first data line and count number of numbers in the line
// works if not tabs ! first replace tabs with spaces... 
// check for multiple spaces... to be done 
  string dataline;
  getline(in,dataline); getline(in,dataline);
  if(dataline.substr(0,1)=="#")dataline=dataline.substr(1,dataline.length());// remove eventual comment from data line
  if(dataline.substr(0,1)==" ")dataline=dataline.substr(1,dataline.length());// remove eventual blank from data, hoping there aren't anymore
  replace( dataline.begin(), dataline.end(),'\t', ' '); // replace all \tabs to spaces
// here counts the numbers
  Int_t nd=0,ind=0,iii=0;
  while(iii!=string::npos){
    iii=dataline.find(" ",ind);
//    cout << iii << " iii\n";
    ind=iii+1;
    nd++;
  } 
//  cout << "nd";

  if(nd==2) cout << "\n\tData type is x,y\n";
  else if(nd==3) cout << "\n\tData type is x,y,dy\n";
  else if(nd==4) cout << "\n\tData type is x,y,dx,dy\n";
  else {
    cout << "\n\tData type is unknown, exit\n";
    return;
  }
   
// close file
  in.close();


// reopen for data reading
  in.open(file.c_str());  
  TString FileName=file;
  

  cout << "\n\tReading Data, ";    
  TGraphErrors *gr;  
  
// plot the measurements reading from file, special case for Data Type x,y,dy 
  if(nd==3)gr = new TGraphErrors(FileName,"\%lg \%lg \%lg");
  else gr = new TGraphErrors(FileName);   
  
// set plot attributes  
  gr->SetTitle(Title.c_str());
  gr->SetMarkerColor(kBlue);
  gr->SetMarkerStyle(21);
  gr->SetLineColor(kRed);
  gr->GetXaxis()->SetTitle(Xtitle.c_str());
  gr->GetYaxis()->SetTitle(Ytitle.c_str());
  
// if default limits, set min and max reading range from plot limits  
  if(min==0 & max==100){
  	min=gr->GetXaxis()->GetXmin();
  	max=gr->GetXaxis()->GetXmax();
  	funzione->SetRange(min,max);
  }
  
  const int npo=gr->GetN();
  cout << "found: " <<  npo << " points\n\t------------------------------\n";        

  const int ndec=abs(log10(max-min));
  if(ndec>maxdec)cout << "\tMany decades found, set log x scale\n\t------------------------------\n"; 

// create and set canvas style
  TCanvas *c1 = new TCanvas("c1",Title.c_str(),10,10,900,700);
  c1->SetFillColor(19);
  c1->SetGrid(1,1); 
  if(makepulls)c1->Divide(1,2);
  c1->cd(1);  
  if(ndec>maxdec)gPad->SetLogx();
  
// set parameter names and initial values
  for (int np=0;np<numpar;np++)funzione->SetParName(np,parnames[np].c_str());
// fit in range and plot
  gr->Fit("funzione","QR");
  
// get fit results and print with better precision   
  TF1 *fr=gr->GetFunction("funzione");
  cout << "\tFit Results\n"; 
  for (int np=0;np<numpar;np++){
    cout << "\t" << parnames[np] << " = " << fr->GetParameter(np) << " +/- " << fr->GetParError(np) <<"\n";
  }
  cout << "\n";
  
  // if a zoom then set the limits also in y 
  if(zoom){
    float ymin=fr->Eval(min);
    float ymax=fr->Eval(max); 
    if(ymin>=ymax){
      float ybuf=ymax;
      ymax=ymin;
      ymin=ybuf;
    }   
    gr->GetXaxis()->SetLimits(min,max);
    gr->GetYaxis()->SetRangeUser(0.95*ymin, 1.05*ymax);  
  }
// now plot   
  gr->Draw("AP");
  c1->Update();
  
  
  if(makepulls){	
// make plot of pulls
	   const int ndof=funzione->GetNDF();	   	   
	   Double_t yy;
       TVectorD pull(npo),xx(npo);

// loop on points
       for (Int_t bin=0;bin<npo;bin++){  
         gr->GetPoint(bin,xx(bin),yy);
// compute the residuals         
         pull(bin) = (yy-funzione->Eval(xx(bin),0.0,0.0));
// Compute now the pulls (normalized residuals) for different cases
// no error case: the estimated error is sigmaest 
// compute the estimated st.dev. by Fisher method: sqrt of (Chi2/Divided by n-2 i.e. NDOF)
// R option is important to compute the Chisquare only for used point
         if(nd==2){
           pull(bin)=pull(bin)/sqrt(gr->Chisquare(funzione,"R")/(ndof));;
         }  
// y error case: the error is given in the data         
         else if(nd==3){
           pull(bin)=pull(bin)/gr->GetErrorY(bin);
         }  
// xy error case: the error is given in the data but the pulls has to be corrected for the x errors:
// when x errors are present, the error along x is projected along the y-direction by calculating 
// the derivative of the function and added in quadrature tyo the y error. it is anyway an approximation 
         else if(nd==4){
           pull(bin)=pull(bin)/sqrt( pow((gr->GetErrorY(bin)),2)+pow(fr->Derivative(xx(bin))*gr->GetErrorX(bin),2)); 
         }       
       } 
// now create the Pulls TGraph		
		TGraph *re = new TGraph(xx,pull);

		re->SetTitle(Title.c_str());
		re->SetMarkerColor(kBlue);
		re->SetMarkerStyle(21);
		re->SetMaximum(5);
		re->SetMinimum(-5);
		re->GetXaxis()->SetTitle(Xtitle.c_str());
        re->GetYaxis()->SetTitle("Residui Normalizzati");
        if(zoom)re->GetXaxis()->SetLimits(min,max);
        
        c1->cd(2);
	    c1->SetGrid(1,1);
	    if(ndec>maxdec)gPad->SetLogx();
		re->Draw("AP");
		
// draw a line on plot at zero 
		TLine *tl;
		tl= new TLine(min,0.0,max,0.0);
		tl->SetLineColor(kRed);
		tl->SetLineWidth(3);
		tl->SetLineStyle(2);
		tl->Draw();
		c1->Update();
  }	


// save the plots in pdf with the same name of the original Input File 
  if(output){
  	FileName.Remove(FileName.Length()-4,FileName.Length());
    c1->Print(FileName+".png"); 
  } 
}

