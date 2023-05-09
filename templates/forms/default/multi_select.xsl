<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="multi-select/identifier" />
        
        <div class="container">
            <div class="form-group">
                
                <label for="{$identifier}">
                    <xsl:value-of select="multi-select/label"/> 
                </label>
                
                <div class="row align-items-center">
                    <div class="col-5">
                        <xsl:if test="multi-select/query">
                            <select class="form-control form-control-sm" 
                                    name="{$identifier}" id="{$identifier}Left">
                                <option></option>
                            </select>
                        </xsl:if>
                        
                        <xsl:if test="multi-select/options">
                            <select multiple="multiple" 
                                    class="form-control form-control-sm" 
                                    name="{$identifier}Left" id="{$identifier}Left">       
                                <xsl:for-each select="multi-select/options/option">
                                    <xsl:variable name="optionValue" select="value" />
                                    <option value="{$optionValue}">
                                        <xsl:value-of select="value"/>
                                    </option>
                                </xsl:for-each>
                            </select>
                        </xsl:if>
                    </div>
                    <div class="col-1">
                        <i class="fas fa-angle-right" onclick="sendToRight('{$identifier}')"></i>
                        <br />
                        <i class="fas fa-angle-left" onclick="sendToLeft('{$identifier}')"></i>
                    </div>
                    <div class="col-5">
                        <select multiple="multiple" 
                                class="form-control form-control-sm" 
                                name="{$identifier}" id="{$identifier}">
                            
                        </select>
                    </div> 
                    <div class="col-1">
                    </div>
                </div>
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="multi-select/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
